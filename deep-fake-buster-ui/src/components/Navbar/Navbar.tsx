import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {faSun} from "@fortawesome/free-solid-svg-icons";
import {faMoon} from "@fortawesome/free-solid-svg-icons";

export const Navbar = ({theme, setTheme}) =>{
    return <div className={"w-full p-5 px-8 flex flex-row items-center justify-between"}>
        <div className={"flex flex-row items-center  space-x-4"}>
            <img width="50" height="50" src="https://img.icons8.com/ios/50/ffffff/spyware-free.png" alt="spyware-free"/>
            <p className={"text-sm text-white font-bold "}>Deep Fake Buster</p>
        </div>
        <FontAwesomeIcon icon={theme ? faSun : faMoon} className={`${theme ? "text-yellow-400" : "text-sky-200"} text-2xl text-white cursor-pointer`} onClick={()=>setTheme(prevState=>!prevState)}/>
    </div>

}