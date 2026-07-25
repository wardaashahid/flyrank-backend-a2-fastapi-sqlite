const express=require("express");
const app =express();
const PORT=3000;

app.get("/",(req,res)=>{
  res.json({
    message:"heyyy"
  });
});

app.get("/About",(req,res)=>{
  res.json({
    name: "Warda",
    course: "AI Backend Assignment I"
  });
});

app.listen(PORT,()=>{
  console.log(`Server is running on http://localhost:${PORT}`);
});

