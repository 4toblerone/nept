$(document).ready(function(){
    var end = false;
	function lastAddedLiveFunc()
	{
		$.get("/return_next_posts/", function(data){
            console.log(data);
            data = JSON.parse(data);//check this out more, is it because of the content type
            console.log(data);
            end = data.end;
			if (data != "") {
				console.log('add data..');
                $.each(data.img_urls, function(i, item){
                    $(".items").append(
                      '<li><img src="'+item+'"/> <div class="fb-share-button" data-href="'+item+'" data-type="button_count"></div><br><li/> '
                    );
                    console.log($(".items").last());
                    //FB.XFBML.parse($(".items").last());//not working why?
                    FB.XFBML.parse();//working
                });
			}
		});
	};

  //lastAddedLiveFunc();
  $(window).scroll(function(){
    if (end == false){
      var wintop = $(window).scrollTop(), docheight = $(document).height(), winheight = $(window).height();
      var  scrolltrigger = 0.95;

      if  ((wintop/(docheight-winheight)) > scrolltrigger) {

         lastAddedLiveFunc();
      }
    }
  });
});
