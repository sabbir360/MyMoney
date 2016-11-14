/**
 * Created by Sabbir on 6/13/2014.
 */

var sweetCore = {

    //initialize start up required functions :)
    _init:function(){
        $(document).ready(function(){
           sweetCore.currentMenuSelector();
        });
    },

    /**
     * Will select current action in menu item as active
     */
    currentMenuSelector : function(){
       /* var selectable = $(".js-menu").attr("data-current-page");
        $("."+selectable).addClass("active-menu");*/

        try{
            var menuItem = document.URL.replace(window.location.protocol+"//"+window.location.host,"");
            menuItem = menuItem.split("?")[0];
            var menuItemLength = menuItem.length;
            if(menuItemLength>0){
                if(menuItem.substring(menuItemLength-1,menuItemLength)!="#"){
                    try{
//                        var activeMenu = jQuery("li [href='"+menuItem+"']").addClass("active-menu");//active menu
                        jQuery("li [href='"+menuItem+"']").parent("li").addClass("active");//active menu
//                        var listOfParents = activeMenu.parents("*");
//                        console.log(listOfParents)
//                        alert(listOfParents.find("a.first").parent().html())
//                        listOfParents.find("a.first").addClass("active-menu-parent");
                    }catch (E){
                        console.log(E)
                    }
                }
            }
        }catch (Ex){
            console.log(Ex)
        }
    },

    loading:function(hide){
        if(hide){
            $(".loading").slideUp("slow");
            return
        }
        $(".loading").slideDown("slow")
    },

    /**
     * Generic delete function using ajax
     * @param url
     * @param id
     */
    deleteAjax:function(selector){
        var form_data = $("."+selector);
        var confirmation = confirm("Are you sure? If deleted you can't roll back!")
        if(confirmation==true){
            sweetCore.loading()
            $.ajax({
            url:form_data.attr("action"),
            type:'post',
            data:form_data.serialize(),
            success:function(response){

                window.location.reload()
                sweetCore.loading(true)
            },error:function(){
                alert("Something went wrong!");
                sweetCore.loading(true)
            }
        });
        }

    }
}

/*

//slickNav
$(function(){
		$('#menu').slicknav();
	});*/
