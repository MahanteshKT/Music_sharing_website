function myFunction(){
    console.log("hello world")
}

const funVisbility=(e)=>{
    let allowed_emails=document.querySelector(".access-emails");
    let Visbility=document.getElementById("visibility").value;
    console.log("protected",Visbility)
    if(Visbility == "protected"){
        console.log("protected",Visbility)
        allowed_emails.style.visibility=`visible`;
    }
    else{
        allowed_emails.style.visibility=`hidden`;

    }
}


// Messages close

const closelogo=document.querySelector(".closelogo");
const message=document.querySelector(".message-alert");

    if(closelogo){
        closelogo.addEventListener("click",function msgclose(){
        message.style.display="none";
        console.log("message close");
    });
    }

var a=setTimeout(function msgclose(){
    if(message){
        message.style.display="none";
        message.style.transition=`0.5s`;
    }
    
    clearTimeout(a);
},4000);




// NAVBAR 
var menubaricon=document.querySelector(".menu-bar-icon");
menubaricon.onclick=function(){
    navLinks=document.querySelector(".header-links");
    navLinks.classList.toggle("active")
    console.log('clicked')
}



var count=0;
var audio=document.getElementById('audio')
var audioPlayerPause=document.getElementById('audioPlayPause')
var audioStop=document.getElementById('audioStop');

if(audioPlayerPause){
    audioPlayerPause.addEventListener('click',function(){
        if(count==0){
            count=1;
            audio.play();
            console.log("count",count)
            audioPlayerPause.innerHTML="<i class='fa fa-pause'></i>";
    
    
            
            var audioList=document.querySelectorAll('.aTrigger');
            audioList.forEach(function(audioSingle,index){
                var dataActive=audioSingle.getAttribute('data-active');
                if(dataActive == "pause"){
                    audioSingle.setAttribute('data-active','active');
    
                }
            })
    
        }else{
            count=0;
            audio.pause();
            audioPlayerPause.innerHTML="<i class='fa fa-play'></i>";
    
            var audioList=document.querySelectorAll('.aTrigger');
            audioList.forEach(function(audioSingle,index){
                var dataActive=audioSingle.getAttribute('data-active');
                if(dataActive == "active"){
                    audioSingle.setAttribute('data-active','pause');
                }
            })
        }
    })

}


if(audioStop){
    audioStop.addEventListener('click',function(){
        count=0;
        audio.pause()
        audio.currentTime=0;
        audioPlayerPause.innerHTML="<i class='fa fa-pause'></i>";
        audioPlayerPause.className="";
        audioStop.className="";
        document.getElementById('audioTitle').innerHTML="&nbsp;"
        document.getElementById('audioVisibility').innerHTML="visible"
        duration.innerHTML="0:00"
        var audioList=document.querySelectorAll('.aTrigger');
            audioList.forEach(function(audioSingle,index){
                var dataActive=audioSingle.getAttribute('data-active');
                if(dataActive == "active" || dataActive == "pause" ){
                    audioSingle.setAttribute('data-active','');
                }
            })
    
    })
}


var audioList=document.querySelectorAll('.aTrigger');
var playbtn=document.querySelectorAll(".play-btn");
audioList.forEach(function(audioSingle,index){
    var dataAudioName= audioSingle.getAttribute("data-audio")
    // var audioName= dataAudioName.substring(dataAudioName.lastIndexOf("/")+1,dataAudioName.length);
    var Each=audioSingle.childNodes[1].childNodes[1].childNodes;
    var playicon=audioSingle.childNodes[1].childNodes[3]
    // console.log(playicon)
    playicon.innerHTML="<i class='fa fa-play'></i>"
    audioSingle.addEventListener('click',function(index){
        thisisAudioSingle=this;
        audioPlayerPause.className="active";
        audioStop.className="active";
        var dataAudio=this.getAttribute('data-audio')
        var dataActive=this.getAttribute('data-active')
        var audioSource=document.getElementById('audioSource')

        audioSource.src=dataAudio;
        document.getElementById("audioTitle").innerHTML=Each[1].innerHTML;
        document.getElementById("audioVisibility").innerHTML=Each[5].childNodes[3].innerHTML;
        playicon.innerHTML="<i class='fa fa-pause'></i>"
        for(let i=0;i<audioList.length;i++){
            
            playbtn[i].innerHTML="<i class='fa fa-play'></i>";
            audioList[i].setAttribute("data-active","");
            playicon.innerHTML="<i class='fa fa-play'></i>"
        }
        if(dataActive ==""){
            count=1;
            audio.load();
            audio.play();
            this.setAttribute("data-active","active");
            audioPlayerPause.innerHTML="<i class='fa fa-pause'></i>"
            playicon.innerHTML="<i class='fa fa-pause'></i>"
        }
        else if(dataActive == "pause"){
            count=1;
            audio.play();
            this.setAttribute("data-active","active");
            audioPlayerPause.innerHTML="<i class='fa fa-pause'></i>"
            playicon.innerHTML="<i class='fa fa-pause'></i>"

        }
        else{
            count=0;
            audio.pause();
            this.setAttribute("data-active","pause");
            audioPlayerPause.innerHTML="<i class='fa fa-play'></i>"
            playicon.innerHTML="<i class='fa fa-play'></i>"
        }

        var duration =document.getElementById('duration');
        setTimeout(function(){
            var s=parseInt(audio.duration % 60);
            var m=parseInt((audio.duration / 60)%60);
            duration.innerHTML=m +":"+ s;
            audio.addEventListener("timeupdate",function(){
                var durationUpdate=document.getElementById("durationUpdate");
                var s=parseInt(audio.currentTime % 60);
                var m=parseInt((audio.currentTime / 60)%60);
                durationUpdate.innerHTML=m+":"+s;
                if(duration.textContent == durationUpdate.textContent){
                    audioPlayerPause.innerHTML="<i class='fa fa-play'></i>"
                    playicon.innerHTML="<i class='fa fa-play'></i>"
                    thisisAudioSingle.setAttribute("data-active","pause");
                    count=0;
                }
            },false)

        },200)

    })
})