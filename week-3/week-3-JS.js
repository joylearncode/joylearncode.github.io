function getData() {
    // 利用fetch進行連線資料
    fetch("https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json").then(function (response) {
        return response.json();
    }).then(function (data) {
        let textNode = document.createElement("div");
        textNode.textContent = data.result.results[0].stitle;
        textNode.classList.add("promote_text");
        document.querySelector(".promote1").appendChild(textNode);
        // 圖片
        let files = data.result.results[0].file;
        const head = "https://";
        console.log(files.split(head)[1]);
        document.querySelector(".promote1").childNodes[1].src = head + files.split(head)[1];


        let textNode1 = document.createElement("div");
        textNode1.textContent = data.result.results[1].stitle;
        textNode1.classList.add("promote_text");
        document.querySelector(".promote2").appendChild(textNode1);
        let files2 = data.result.results[1].file;
        const head2 = "https://";
        console.log(files2.split(head2)[1]);
        document.querySelector(".promote2").childNodes[1].src = head2 + files2.split(head2)[1];

        for (let i = 0; i < 11; i++) {
            let node = document.createElement("div");
            node.textContent = data.result.results[i+2].stitle;
            let files = data.result.results[i+2].file;
            const head = "https://";
            console.log(files.split(head)[1]);
            node.classList.add("photo_title");
            document.querySelectorAll(".photo_body")[i].appendChild(node);
            document.querySelectorAll(".photo_body")[i].childNodes[1].src = head + files.split(head)[1];
        }
    });
}

window.onload = getData;