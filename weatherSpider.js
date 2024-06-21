async function loadFile(file) {
    let text = await (new Response(file)).text();
    console.log(text)
    var res = text.split("\r\n")
    console.log(res)
    var time = [];
    var rain = [];
    for (i in res) {
        //console.log(i)
        time.push(res[i].split("-")[0])
        rain.push(res[i].split("-")[1])
    }
    console.log(time)
    console.log(rain)

    var playSpeed=Number(document.getElementById("speedText").value)
    console.log(playSpeed)
    var echart = echarts.init(document.getElementById("map"), 'infographic')
    var curCnt=0
    function refreshMap(){
        var option = {
            timeline: {
                data: time,
                //label: "asd",
                //autoPlay: false,
                //playInterval: 1000
            },
            options: [{
                tooltip: {
                    show: true,
                },
    
                roamController: {
                    show: true,
                    x: "right",
                },
    
                dataRange:{
                    text:['25','0'],
                    calculable:true,
                    min:0,
                    max:25,
                    x:"left"
                },
                
                title: {
                    text:"广州降水",
                    subtext: time[curCnt],
                },
                series: [
                    {
                        name: time[curCnt],
                        type: 'map',
                        data: [{ name: "广州市", value: rain[curCnt], selected: false }],
                        mapType: '广东'
                    }
                ]
            },
            ]
        };
        echart.setOption(option)
        curCnt+=1;
        if(curCnt==time.length)
            {
                curCnt=0
            }
    }

    var isPlaying=false
    refMapIntv=setInterval(refreshMap,playSpeed)
    isPlaying=true
        
    document.getElementById("stopBut").onclick=function(){
        if(isPlaying){
            clearInterval(refMapIntv)
            isPlaying=false
        }
    }

    document.getElementById("startBut").onclick=function(){
        if(!isPlaying){
            refMapIntv=setInterval(refreshMap,playSpeed)
            isPlaying=true
        }
    }

    document.getElementById("leftBut").onclick=function(){
        curCnt-=2
        refreshMap()
    }

    document.getElementById("rightBut").onclick=function(){
        refreshMap()
    }

    console.log("done")
}
