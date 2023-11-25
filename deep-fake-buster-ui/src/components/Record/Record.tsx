import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {faCheck} from "@fortawesome/free-solid-svg-icons";
import {faXmark} from "@fortawesome/free-solid-svg-icons";
import {Button} from "@mui/material";
import DeletIcon from "@mui/icons-material/Delete";
import LinearProgress from '@mui/material/LinearProgress';

export const Record = (props:any) =>{

    console.log(props.progress)

    return <div className={"w-[95%] flex flex-row items-center justify-between p-4 bg-gray-50 rounded-xl"}>
        <div>{props.videoName}</div>
        <div className={"flex flex-row items-center justify-between"}>
            {
                props.progress ? <LinearProgress className={"w-[10vh]"}/> : (props.showDeleteBtn ? <Button
                    startIcon={<DeletIcon/>}
                    variant={"text"}
                    color={"error"}
                    onClick={() => props.handleDelete(props.videoName)}
                ></Button> :  <div className={"flex flex-row items-center"}>
                    <div className={`${props.result ? "bg-green-50" : "bg-rose-50"} rounded-full w-[30px] h-[30px] flex flex-col items-center justify-center mr-4`}>
                        <FontAwesomeIcon icon={props.result ? faCheck : faXmark} className={`${props.result ? "text-green-500" : "text-red-500"} text-lg`}/>
                    </div>
                    <div>{props.result === null ? "" : props.result ? "Real": "Fake"}</div>
                </div>)
            }



        </div>
    </div>


}