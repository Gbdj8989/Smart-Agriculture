const sidebar=[
    {
        title : "Home",
        path : "/",
        icon : "fa-home",
        cName: "button home"
    },
    {
        title : "Irrigation",
        path : "/irrigation",
        icon : "fa-tint",
        cName: "button water"
    },
    {
        title : "Crop Health",
        path : "/cropHealth",
        icon : "fa-leaf",
        cName: "button health"
    },
    {
        title : "Disease Detection",
        path : "/diseaseDetection",
        icon : "fa-stethoscope",
        cName: "button detection"
    },
    {
        title : "Weather",
        path : "/weather",
        icon : "fa-cloud",
        cName: "button detection"
    }

]
sidebar.map((item,index)=>{
    return(
        document.getElementById("menu")
        .innerHTML+=`<a href="${item.path}" style="text-decoration: none;">
        <div class="${item.cName}">
            <li key=${index}>
                <span><i class="fa ${item.icon}"></i></span>
                <span>${item.title}</span>
            </li>
        </div>
        </a>`
    )
                    
})

