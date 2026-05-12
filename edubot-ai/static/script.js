async function sendMessage(){

    const input = document.getElementById("user-input");
    const chatBox = document.getElementById("chat-box");

    const message = input.value;

    if(message.trim() === ""){
        return;
    }

    // tampilkan pesan user
    chatBox.innerHTML += `
        <div class="message user">
            ${message}
        </div>
    `;

    input.value = "";

    // kirim ke backend
    const response = await fetch("/chat", {

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify({
            message:message
        })
    });

    const data = await response.json();

    // tampilkan balasan bot
    chatBox.innerHTML += `
        <div class="message bot">
            ${data.reply}
        </div>
    `;

    // auto scroll
    chatBox.scrollTop = chatBox.scrollHeight;
}