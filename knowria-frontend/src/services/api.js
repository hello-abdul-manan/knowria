import axios from "axios";

// Create Axios instance with backend base URL
const API = axios.create({
    baseURL: "http://127.0.0.1:8000",
});

// Upload file to backend
export const uploadFile = (file) => {
    const formData = new FormData();
    formData.append("file", file);

    return API.post("/upload", formData);
};

// Send question to backend
export const askQuestion = (question) => {
    return API.get("/query", {
        // Add query parameter
        params: {question},
    });
};
