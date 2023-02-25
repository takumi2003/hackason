import "./sapporo.css"


const Sapporo = () => { 
    const name = "札幌ドーム";
    const adress = "〒062-0045 北海道札幌市豊平区羊ケ丘１"
    const team = "コンサドーレ札幌";
    const img = "/sapporo.jpg";
    

   return (
      <>
   <div class="flex-container">
   <div class="Visual">
       <h1>{name}</h1>
       <h1>所在地:{adress}</h1>
           <h1>ホームチーム：{team}</h1>
   </div>
   <img src={img} alt="スタジアム" />
</div>
<div class="flex01">
   <div class="warp_text">
       <div class="warp_heading">
           総合
       </div>
       <div class="warp">
           <input type="text" class="textbox"/>
       </div>
   </div>
   <div class="warp_text">
       <div class="warp_heading">
           立地・利便性
       </div>
       <div class="warp">
           <input type="text" className="textbox"/>
       </div>
   </div>
   <div class="warp_text">
       <div class="warp_heading">
           見やすさ
       </div>
       <div class="warp">
           <input type="text" class="textbox"/>
       </div>
   </div>
</div>
<div class="flex02">
   <div class="warp_text">
       <div class="warp_heading">
           グルメ
       </div>
       <div class="warp">
           <input type="text" class="textbox"/>
       </div>
   </div>
   <div class="warp_text">
       <div class="warp_heading">
           熱狂度
       </div>
       <div class="warp">
           <input type="text" class="textbox"/>
       </div>
   </div>
   <div class="warp_text02">
       <div class="messeage">
           感想
       </div>
       <div class="warp">
           <input type="text" class="textbox"/>
       </div>
   </div>
</div>
</>
   )
};

export default Sapporo;
