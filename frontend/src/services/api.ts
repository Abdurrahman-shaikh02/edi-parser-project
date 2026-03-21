export async function validateEDI(file: File) {
  const formData = new FormData()
  formData.append("file", file)

  const res = await fetch("http://127.0.0.1:8000/validate/", {
    method: "POST",
    body: formData
  })

  return res.json()
}
