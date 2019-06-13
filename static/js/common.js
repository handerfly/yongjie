
  $(function(){
    //导航下拉
    $(".nav li").hover(function(){
      $(this).toggleClass("hover").find('.subnav').stop().slideToggle('fast');
    })

    //首页banner
    var banner = new Swiper('.banner', {
      pagination: {
        el: '.banner-pagination',
        clickable :true,
      },
    });

    //报价框弹出层
    $('.quote').click(function(){
      var index = layer.open({
        type: 1,
        closeBtn: 2,
        title: ['快速获取报价', 'font-size:22px;color:#fff;height:50px;line-height:50px;text-align:center;background: #00469c;padding:0'],
        anim: 2,
        shade:0.7,
        area: '600px',
        content: $("#dialog").html(),
        success:function(){
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
              url:"/home/price",
              dataType:'json',
              data:$(".bjbox").serialize(),
              success:function(data){
                if(data.status=="success"){
                    layer.msg('提交成功，请您注意查收短信！');
                    layer.close(index);
                    $(".submit").removeAttr("disabled").text("点击获取");

                }else if(data.status=="fail"){
                    layer.msg('请您正确填写表单！');
                    $(".tip").html("请您正确填写表单！");
                }

              }
            })
          })
        }
      });
    })

    
    

    //在线客服
    $(".onlinebox").click(function(){
      $(this).hasClass('online-show') ? $(this).removeClass("online-show").find('.bd').css('display','none') : $(this).addClass("online-show").find('.bd').css('display','block')
    })

    //导航条固定
    $(window).scroll(function(){
      if($(document).scrollTop()>=154){
        $(".nav").css({"position":"fixed","z-index":999,"left":"0","right":"0","top":"0","margin":"atuo"});
      }else{
        $(".nav").css("position","relative");
      }
    })

    //内页产品轮播
    var peoimgs = function(){
        var j = 0;
        var len = $('.bfocus li').length;
        var nums = $('<div class="num_nav"></div>');
        for(var i=0;i<len;i++){
          nums.append("<span>i</span>");
        }
        nums.find("span").first().addClass("selected").siblings().removeClass("selected");
        $(".imgs_tab").append(nums);	
        function move(){
          $('.bfocus li').eq(j).fadeIn().siblings().fadeOut();
          $('.num_nav').find("span").eq(j).addClass("selected").siblings().removeClass("selected");
        }
        $('.next').click(function(){
          j++;
          if(j >= len){
            j = 0;
          }
          move();
        })  
        $('.prev').click(function(){
          j--;
          if(j <= -1){
            j = len - 1;
          }
          move();
        })  
        $('.num_nav').find("span").hover(function(){
          j=$(this).index();
          move();
        })  
        var timer = null;
        timer = setInterval(function(){
          j++;
          if(j>=len){
            j = 0
          }
          move();
        },2000)
        $('.imgs_tab').mouseover(function(){
          clearInterval(timer);
        })
        $('.imgs_tab').mouseout(function(){
          timer = setInterval(function(){
            j++;
            if(j>=len){
              j = 0
            }
            move();
          },2000)
        })
    }
    peoimgs();


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

 

    $(".catelist a").click(function(){
      $(this).addClass("active").siblings().removeClass("active");
      var tid = $(this).attr('data-id');
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
