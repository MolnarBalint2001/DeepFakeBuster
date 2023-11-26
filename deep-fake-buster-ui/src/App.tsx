
import './App.css'
import {Header} from "./components/Header/Header.tsx";
import {TestDatagrid} from "./components/TestDatagrid/TestDatagrid.tsx";
import {useEffect, useState} from "react";

const App = () =>{

    const [theme, setTheme] = useState<boolean>(true);

    return (
        <div className={`${theme ? "bg-white" : "bg-slate-900"} grid grid-cols-1 place-items-center h-fit`}>
            <Header theme={theme} setTheme={setTheme}/>
            <TestDatagrid theme={theme}/>
        </div>

    )



}

export default App;