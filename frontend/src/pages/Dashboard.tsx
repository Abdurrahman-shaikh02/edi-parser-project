import { useState } from "react"
import FileUpload from "../components/FileUpload"
import ErrorPanel from "../components/ErrorPanel"

export default function Dashboard() {
  const [errors, setErrors] = useState([])

  return (
    <div style={{ padding: "20px" }}>
      <h1>EDI Debugger</h1>

      <FileUpload onResult={setErrors} />

      <ErrorPanel errors={errors} />
    </div>
  )
}
