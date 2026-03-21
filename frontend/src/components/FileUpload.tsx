import { validateEDI } from "../services/api"

export default function FileUpload({ onResult }: any) {
  const handleUpload = async (e: any) => {
    const file = e.target.files[0]
    if (!file) return

    const data = await validateEDI(file)
    console.log("API RESPONSE:", data)
    onResult(data.errors)
  }

  return (
    <div>
      <input type="file" onChange={handleUpload} />
    </div>
  )
}
