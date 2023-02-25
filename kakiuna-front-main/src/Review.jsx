import { useState } from "react";
const Review = () => {

    const [text, setText] = useState("");
    const [all,setAll] = useState("");
    const [convenient,setConvenient] = useState("");
    const [ableSee, setAbleSee] = useState("");
    const [gourmet, setGourmet] = useState("");
    const [excited, setExcited] = useState("");


    const [addtext, setAddText] = useState("");
    const [addAll, setAddAll] = useState("");
    const [addConvenient,setAddConvenient] = useState("");
    const [addAbleSee, setAddAbleSee] = useState("");
    const [addGourmet, setAddGourmet] = useState("");
    const [addExcited, setAddExcited] = useState("");

    const onClickAddScreen = () => {
        setAddText(text);
        setAddAll(all);
        setAddConvenient(convenient);
        setAddAbleSee(ableSee);
        setAddGourmet(gourmet);
        setAddExcited(excited);

        setText("");
        setAll("");
        setConvenient("");
        setAbleSee("");
        setGourmet("");
        setExcited("");
    }

    return (
        <>
    <div>
        <p>スタジアム名</p>
        <input type="text" value={text} onChange={(event) => setText(event.target.value)}/>
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
       <input type="text" value={convenient} onChange={(event) => setConvenient(event.target.value)}/>
       </div>
   </div>
   <div class="warp_text">
       <div class="warp_heading">
           見やすさ
       </div>
       <div class="warp">
       <input type="text" value={ableSee} onChange={(event) => setAbleSee(event.target.value)}/>
       </div>
   </div>
</div>
<div class="flex02">
   <div class="warp_text">
       <div class="warp_heading">
           グルメ
       </div>
       <div class="warp">
       <input type="text" value={gourmet} onChange={(event) => setGourmet(event.target.value)}/>
       </div>
   </div>
   <div class="warp_text">
       <div class="warp_heading">
           熱狂度
       </div>
       <div class="warp">
       <input type="text" value={excited} onChange={(event) => setExcited(event.target.value)}/>
       </div>
   </div>
   <div class="warp_text02">
       <div class="messeage">
           感想
       </div>
       <div class="warp">
        <input type="text" value={excited} onChange={(event) => setExcited(event.target.value)}/>
       </div>
   </div>
</div>
<button onClick={onClickAddScreen}>決定</button>
        </>
    )
    }

export default Review;
