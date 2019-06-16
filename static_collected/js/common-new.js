
  $(function(){
    //导航
    $(".navBtn").click(function(){
      if($(this).hasClass("wapBtnAn")){
        $(this).removeClass("wapBtnAn");
        $(".nav").css({"right":'-125px',"display":"none","height":"100%",'z-index':999})
      }else{
        $(this).addClass("wapBtnAn");
        $(".nav").css({"right":0,"display":"block","height":"100%",'z-index':999})
      }
    })

    $(".nav li").click(function(){
      $(this).addClass("active").siblings().removeClass("active");
      var tid = $(this).attr("data-id");
      if(tid){
        $(".branchlist").find("ul[data-cid='" + tid + "']").show().siblings().hide();
      }else{
        $(".branchlist").find("ul").hide();
      }

    })

    //首页banner
    var banner = new Swiper('.banner', {
      pagination: {
        el: '.banner-pagination',
        clickable :true,
      },
    });


    //首页tab
    $(".news-panel .hd a").click(function(){
      $(this).addClass("active").siblings().removeClass("active")
      $(".news-panel .news").find("ul").eq($(this).index()).show().siblings().hide()
    })

    //报价框弹出层
    //表单验证
    $(".submit").click(function(){

      if($('input[name="area"]').val() == ""){
        layer.msg('请输入车间面积');
        return;
      }
      if($('select[name="level"]').val() == ""){
        layer.msg('请选择净化级别');
        return;
      }
      if($('input[name="name"]').val() == ""){
        layer.msg('请输入您的姓名');
        return;
      }
      if($('input[name="sex"]').val() == ""){
        layer.msg('请选择性别');
        return;
      }
      var phone = $('input[name="mobile"]').val();
      if(phone == "" || !(/^1(3|4|5|7|8)\d{9}$/.test(phone))){
        layer.msg('请输入正确的手机号');
        return;
      }
      $(this).attr("disabled","").text("正在发送");
      $.ajax({
        type:"POST",
        url:"http://www.aaa.com/aaa",
        data:$(".bjbox").serialize(),
        success:function(res){
          layer.msg('提交成功，请注意查收短信！');
          $(".submit").removeAttr("disabled").text("点击获取");
        }
      })
    })




    //内页产品轮播
    var pics = new Swiper('.pics', {
      pagination: {
        el: '.pics-pagination',
        clickable :true,
      },
    });


    //案例页介绍
    $(".showmore").click(function(){
      if($(this).attr('data-v') == 0){
        $(this).parent().find(".intro").hide();
        $(this).parent().find(".desc").show();
        $(this).attr('data-v',1).html("<i>-</i>收起")
      }else{
        $(this).parent().find(".intro").show();
        $(this).parent().find(".desc").hide();
        $(this).attr('data-v',0).html("<i>+</i>更多介绍")
      }
    })

    $(".catelist li").click(function(){
      $(this).addClass("active").siblings().removeClass("active");
      var tid = $(this).find("a").attr('data-id');
      if(tid == 0){
        $('.list').find("li").show();
      }else{
        $('.list').find("li").hide();
        $('.list').find("li[data-cid='" + tid + "']").show()
      }
    })


    //案例详情tab
    $(".case_detail .tit span").click(function(){
      $(this).addClass("active").siblings().removeClass("active");
      if($(this).attr('data-rel') == 'desc'){
        $(".case_detail").find(".desc").removeClass("hide");
        $(".case_detail").find(".app_prod").addClass("hide");
      }else{
        $(".case_detail").find(".desc").addClass("hide");
        $(".case_detail").find(".app_prod").removeClass("hide");
      }
    })

    //荣誉资质弹出层
    $("a[parm='bigpic']").fancybox();
  })
