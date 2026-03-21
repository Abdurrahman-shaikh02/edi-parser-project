import { useState } from "react";
import axios from "axios";

export default function Home() {
  const [file, setFile] = useState<File | null>(null);
  const [result, setResult] = useState<any>(null);

  const handleUpload = async () => {
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    const res = await axios.post("http://localhost:8000/api/parse", formData);

    setResult(res.data);
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>EDI Parser Demo</h1>

      <input type="file" onChange={(e) => setFile(e.target.files?.[0] || null)} />
      <button onClick={handleUpload}>Upload</button>

      {result && (
        <div>
          <h2>Transaction Type</h2>
          <p>{result.detection.description}</p>

          <h2>Errors</h2>
          {result.fixes.map((e: any, i: number) => (
            <div key={i} style={{ border: "1px solid red", margin: "10px", padding: "10px" }}>
              <p><b>Segment:</b> {e.segment}</p>
              <p><b>Error:</b> {e.message}</p>
              <p><b>Fix:</b> {e.suggestion}</p>
            </div>
          ))}

          <h2>Segments</h2>
          <pre style={{ maxHeight: "300px", overflow: "scroll" }}>
            {JSON.stringify(result.segments, null, 2)}
          </pre>
        </div>
      )}
    </div>
  );
}
