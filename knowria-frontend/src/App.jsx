import Upload from "./components/Upload";
import Chat from "./components/Chat";

export default function App() {
  return (
    <div style={{ padding: "20px" }}>
      <h1>Knowria AI</h1>
      <Upload />
      <hr />
      <Chat />
    </div>
  );
}
