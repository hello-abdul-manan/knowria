import { useState } from "react";
import { askQuestion } from "../services/api";

export default function Chat() {
  // Store user input and chat messages
  const [question, setQuestion] = useState("");
  const [messages, setMessages] = useState([]);

  // Handle sending question and updating chat
  const handleAsk = async () => {
    if (!question) return;

    const userMessage = { role: "user", content: question };
    setMessages((prev) => [...prev, userMessage]);

    // Call backend and add bot response
    const res = await askQuestion(question);
    const botMessage = {
      role: "bot",
      content: res.data.answer,
    };
    setMessages((prev) => [...prev, botMessage]);

    setQuestion("");
  };

  return (
    <div>
      <h2>Chat</h2>

      <div
        style={{
          border: "1px solid #ccc",
          padding: "10px",
          height: "300px",
          overflowY: "scroll",
        }}
      >
        {messages.map((msg, index) => (
          <div key={index}>
            <strong>{msg.role}:</strong> {msg.content}
          </div>
        ))}
      </div>

      <input
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        placeholder="Ask something..."
      />
      <button onClick={handleAsk}>Send</button>
    </div>
  );
}
