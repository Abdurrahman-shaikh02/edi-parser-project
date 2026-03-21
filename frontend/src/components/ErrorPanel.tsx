export default function ErrorPanel({ errors }: any) {
  if (!errors || errors.length === 0) return <p>No errors</p>

  return (
    <div>
      {errors.map((err: any, i: number) => (
        <div key={i} style={{ marginBottom: "20px" }}>
          <p>❌ {err.message}</p>
          <p>💡 {err.suggestion}</p>
          <p>🤖 {err.ai_explanation}</p>
        </div>
      ))}
    </div>
  )
}
