# 一：下载本安装脚本（目前版本: ECE-2.4.3, 系统要求: centos7）
# 二：安装前的准备工作
### 1. ansible 安装(版本大于2.5)
### 2. docker 的 rpm 安装包准备（下载参看安装包内的download.sh）, 并且移动到 roles/install_docker/files/ 文件夹下
    containerd.io-1.2.2-3.3.el7.x86_64.rpm
    docker-ce-18.09.2-3.el7.x86_64.rpm
    docker-ce-cli-18.09.2-3.el7.x86_64.rpm
### 3. ece 的 docker 镜像tar包准备（下载参看安装包内的download.sh）, 并且移动到 roles/install_registry/files/ 文件夹下
    如果已经有自己的内部镜像仓库，请自行上传docker的镜像文件到内部仓库
    elasticsearch.6.8.5-0.tar
    kibana.6.8.5-0.tar
    apm.6.8.5-0.tar
    elasticsearch.7.5.0-0.tar
    kibana.7.5.0-0.tar
    apm.7.5.0-0.tar
    app-search.7.5.0-0.tar
    elasticsearch.7.6.0-0.tar
    kibana.7.6.0-0.tar
    registry.tar

# 三：配置安装脚本
### 1. 修改安装脚本里面的 hosts 文件，配置项有明确注释
```bash
# 1.1 设置服务器列表, zone(可用区), management(是否管理节点), tags(给节点打标签格式：key:value,key:value)
ece01 ansible_ssh_user=root ansible_ssh_pass=123456 zone=MY_ZONE-1 management=1 tags=ssd:true,role:management
ece02 ansible_ssh_user=root ansible_ssh_pass=123456 zone=MY_ZONE-2 management=1 tags=ssd:true,role:management
ece03 ansible_ssh_user=root ansible_ssh_pass=123456 zone=MY_ZONE-3 management=1 tags=ssd:true,role:management
# 1.2 设置第一个安装节点
[ece_first_node]
ece01
# 1.3 设置其他安装节点
[ece_other_node]
ece02
ece03
# 1.4 设置镜像仓库
[registry]
ece01
```
### 2. 修改安装脚本里面的 roles/common/defaults/main.yml 文件，配置项有明确注释
```bash
# docker 镜像仓库地址, like: 172.31.23.63:5000
docker_registry: TODO
# docker 镜像仓库所在子目录(避免命名冲突, 效果：172.31.23.63:5000/inner/cloud-assets/elasticsearch:7.2.0-0)
docker_registry_path: /inner
# coordinator 节点，可以直接设置成第一台ece节点的ip
coordinator_host: TODO
# 数据盘挂载点 PLEASE CHECK
mount_dir: /data
# 是否格式化并挂载数据盘(该脚本不支持超过2T数据盘, 可选参数：True, False)
need_mount: False
```
### 3. 用 ansible ping 一下确保连通性
```bash
ansible all -m ping -i hosts
```

# 四：安装 ECE 集群
### 1. 启动安装脚本

```bash
# 完整安装(可重复跑，直到整个机器都完成安装，会自动跳过安装成功的节点。正式环境可选择跳过安装镜像仓库，使用公司自己部署的。reboot 不建议 skip。)
# 可选参数: --skip-tags "install_registry,reboot"
ansible-playbook install.yml -i hosts
```

### 2. 等待安装完成，注意保存集群的账户信息

```bash
# 如果忘记保存了，可以通过以下命令重新获取账号相关信息
ansible ece_first_node -m shell -a 'sed -r "s/\x1B\[([0-9]{1,2}(;[0-9]{1,2})?)?[m|K]//g" /home/elastic/ece.log' -i hosts
```

# 五：登入 ECE 管理后台，进行管理操作

### 1. 扩容 admin-console-search 集群为 3 个 zone
### 2. 扩容 logging-and-metrics 集群为 3 个 zone，每个节点内存为 4 GB

# 六：未来的集群扩容操作
### 1. 修改安装脚本里面的 hosts 文件（这里只会用到 add_nodes 分组）
### 2. 启动扩容安装脚本

```bash
ansible-playbook add_nodes.yml -i hosts
```

# 七：问题汇总
* ansible 服务器缺少其他机器的 known_hosts 记录, 报连接错误, 可以通过执行下面命令跳过这个检查
```bash
export ANSIBLE_HOST_KEY_CHECKING=False
```

* 如果要重装某个ece节点，请先登录这台服务器进行清理操作(请慎重，这个节点会被直接干掉)
```bash
# 如果是已经加入到机器的节点, 记得到ece管理后台把对应的runner也要删掉
# /data/elastic/目录对应安装时候设置的host_storage_path
docker rm -f frc-runners-runner frc-allocators-allocator $(docker ps -a -q); sudo rm -rf /data/elastic/ && docker ps -a
```

* 安装的时候Checking OS kernel cgroup.memory会有提示未配置
```bash
# 安装的时候跳过重启才会有这个提示，可以重启一下或者执行以下命令检测是否有cgroup.memory=nokmem
/sbin/grubby --info=ALL
```

* 安装其他机器及扩容时候用到的 token 在哪
```
roles/common/defaults/token.json
```

* 安装失败
```
时间不同步有可能导致安装失败, 请 check 所有服务器时间
ansible -i hosts -m shell -a "date -R" all
```

# 八: ES集群访问方式

* 方案1： 通过X-Found-Cluster头信息指定集群ID
```
curl <proxy_ip>:9200/filebeat*/_search\
  -X GET\
  -H 'X-Found-Cluster: <cluster_id>'\
  -H 'Content-Type: application/json'\
  -u user:password\
  -d '{"size": 1}'
```

方案2： 通过绑定host来指定集群ID
```
echo '<proxy_ip>  <cluster_id>.domain.com' >> /etc/hosts
curl <cluster_id>.domain.com:9200/filebeat*/_search\
  -X GET\
  -H 'Content-Type: application/json'\
  -u user:password\
  -d '{"size": 1}'
```

# 九：调整节点的内存配额
```
curl -X PUT \

  http(s)://<ece_admin_url:port>/api/v1/platform/infrastructure/allocators/<allocator_id>/settings \
  -H 'Authorization: Basic <login:pwd base64 encoded>' \
  -H 'Content-Type: application/json' \
  -d '{"capacity":<Capacity_Value_in_Mb>}'
```
