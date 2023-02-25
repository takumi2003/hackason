import { useState } from "react";
import "./App.css";
import Sapporo from "./Sapporo";
import Review from "./Review";
import Login from "./Login";
import Register from "./Register";

import { Route, Routes, Link } from "react-router-dom";

const stadiumValue = [
  { path: "/sapporo", Component: Sapporo },
  //{ path: "/aomori", Component: Aomori },
];

const Home = () => {
  return (
    <div className="html">
      
      <Routes>
        <Route exact path="/login" element={<Login/>} />
        <Route exact path="/review" element={<Review />} />
        <Route exact path="/register" element={<Register />} />
        <Route exact path="/" element={<HomeElement />} />
        {/* <Route exact path="/sapporo" element={<Value.Component />} /> */}
        {stadiumValue.map((Stadiums) => (
          <Route exact path={Stadiums.path} element={<Stadiums.Component />} key={Stadiums.path} />
        ))}
      </Routes>
    </div>
  );
};

function HomeElement() {
  return (
    <div>
      <header>
        <Link to="/review">
          <p>レビューをする</p>
        </Link>

        <Link to="/login">
          <p>ログイン</p>
        </Link>

        <Link to="/register">
          <p>会員登録</p>
        </Link>
        
        <Link to="/">
          <p>ログアウト</p>
        </Link>

      </header>

      <div className="box">
        <h1>
          <Link to="/sapporo">
            <p>札幌ドーム</p>
          </Link>
        </h1>
        <p>☆☆☆☆☆</p>
      </div>
    </div>
  );
}

export default Home;
