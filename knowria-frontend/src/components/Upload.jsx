import { useState } from "react";
import { uploadFile } from "../services/api";

// Upload document component
export default function Upload() {
    // Store selected file
    const [file, setFile] = useState(null)

    const handleUpload = async () => {
        // Prevent empty upload
        if (!file) return;

        // Send file to backend
        await uploadFile(file);
        alert("File uploaded successfully!")
    };

    return (
        <div>
            <h2>Upload Document</h2>

            <input type="file" 
            onChange={(e) => setFile(e.target.files[0])} />
            <button onClick={handleUpload}>Upload</button>
        </div>
    )
}