
import {Navbar} from "../Navbar/Navbar.tsx";

export const Header = () =>{



    return (
        <div className={"h-[30vh] w-full bg-gradient-to-bl from-[#3b82f6] to-[#1e40af] flex flex-col justify-content-center align-items-center"}>
            <Navbar/>
            <div className={"m-2 space-y-2"}>
                <div className={"text-white font-bold text-3xl drop-shadow-lg text-center"}>Deep Fake Buster</div>
                <div className={"uppercase font-bold text-white text-lg drop-shadow-lg text-center"}>By TEAM ALSET</div>
            </div>
        </div>
    )

}