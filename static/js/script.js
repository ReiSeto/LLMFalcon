async function sendMessage() {
    const userInput = document.getElementById("userInput");
    const chatBody = document.getElementById("chatBody");

    const userMessage = userInput.value;
    if (userMessage.trim() === "") return;
    userInput.value = "";

    const userMessageElement = document.createElement("div");
    userMessageElement.classList.add("chat-message", "user");
    userMessageElement.innerHTML = `<span>${userMessage}</span>`;
    chatBody.appendChild(userMessageElement);

    chatBody.scrollTop = chatBody.scrollHeight;

    // Gửi câu hỏi đến API Flask
    try {
        const response = await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ query: userMessage })
        });

        const result = await response.json();
        const botMessage = result.answer;

        const botMessageElement = document.createElement("div");
        botMessageElement.classList.add("chat-message", "bot");
        botMessageElement.innerHTML = `<span>${botMessage}</span>`;
        chatBody.appendChild(botMessageElement);

        chatBody.scrollTop = chatBody.scrollHeight;
    } catch (error) {
        console.error("Error:", error);
    }
}
