import { useState } from "react";
import Home from "./Home";
import { Route, Routes, Link } from "react-router-dom";

const Register = () => {
    const [username, setUserName] = useState();
    const [mail, setMail] = useState("");
    const [passward, setPassward] = useState("");
    const [passward2, setPassward2] = useState("");

    const [addMail, setAddMail] = useState("");
    const [addpassward, setAddPassward] = useState("");
    const [addpassward2, setAddPassward2] = useState("");

    const onClickSubmit = () => {
        setUserName(username);
        setAddMail(mail);
        setAddPassward(passward);
        setAddPassward2(passward2);
    }
    return (
        <>
        <Routes>
        < Route exact path="/nowlogin" element={<Home />} />
        </Routes>

        <div class="content">
        <h1>入会申し込み</h1>
        <p>入会するには次のフォームに必要事項をご記入ください</p>
        <div class="control">
            <label >ユーザーネーム <spam class="required">必須</spam></label>
            <input type="email" value={username} onChange={(event) => setUserName(event.target.value)}/>
        </div>
        <div class="control">
            <label for="mymail">メールアドレス <spam class="required">必須</spam></label>
            <input type="email" value={mail} onChange={(event) => setMail(event.target.value)}/>
        </div>
        <div class="control">
            <label for="password">パスワード <spam class="required">必須</spam></label>
            <input type="password" value={passward} onChange={(event) => setPassward(event.target.value)}/>
        </div>
        <div class="control">
            <label for="password2">パスワード(確認) <spam class="required">必須</spam></label>
            <input type="password" value={passward2} onChange={(event) => setPassward2(event.target.value)}/>
        </div>
        <Link to="/nowlogin">
            <button onClick={onClickSubmit} type="submit">登録する</button>
        </Link>
    </div>
     </>
    )
}

export default Register;
