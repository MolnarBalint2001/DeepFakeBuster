import {Dialog, DialogContent, DialogTitle, Tooltip, Typography} from "@mui/material";
import DeleteIcon from "@mui/icons-material/Delete";
import CloseIcon from "@mui/icons-material/Close";
import LinearProgress from '@mui/material/LinearProgress';
import React, {useState} from "react";
import SyntaxHighlighter from 'react-syntax-highlighter';
import {docco} from 'react-syntax-highlighter/dist/esm/styles/hljs';
import IconButton from '@mui/material/IconButton';
import InfoIcon from '@mui/icons-material/Info';
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {faCheck} from "@fortawesome/free-solid-svg-icons";
import {faClose} from "@fortawesome/free-solid-svg-icons";

export const Record = (props: any) => {

    const [open, setOpen] = useState<boolean>(false);

    return <>
        <div
            onClick={() => {
                if (props.failes?.length > 0) {
                    setOpen(true);
                }
            }}
            className={`w-[95%] ${props.result === null ? `${props.theme ? "bg-slate-50 border-slate-100" : "bg-slate-800 border-slate-700"} ` : props.result ?  `${props.theme ? "bg-green-50 border-green-200" : "bg-green-700 border-green-500"}` : `${props.theme ? "bg-red-50 border-red-100" : "bg-red-700 border-red-500"} `} h-[6vh] flex flex-row p-1 px-2 justify-between items-center border-[1px] rounded-md cursor-pointer`}>
            <div className={`${props.theme ? "text-black" : "text-slate-400"}`}>{props.videoName}</div>
            <div className={"flex flex-row items-center justify-between"}>
                {
                    props.progress ? <LinearProgress className={"w-[10vh]"}/> : (props.uploadState ? <IconButton
                                color={"error"}
                                onClick={() => props.handleDelete(props.videoName)}
                            >
                                <DeleteIcon/>
                            </IconButton> :
                            <div className={"flex flex-row items-center space-x-2"}>
                                <FontAwesomeIcon icon={props.result ? faCheck : faClose} className={`${props.result ? `${props.theme ? "text-green-600" : "text-green-50"}` : `${props.theme ? "text-red-600" : "text-red-50"}`}`}/>
                                <div className={`${props.result ? `${props.theme ? "text-green-600" : "text-green-50"}` : `${props.theme ? "text-red-600" : "text-red-50"} font-medium`}`}>{props.result === null ? "" : props.result ? "Passed" : "Failed"}</div>
                            </div>

                    )
                }
            </div>
        </div>
        <Dialog open={open} sx={{

        }} onClose={() => setOpen(false)}>
            <DialogTitle className={"flex flex-row items-center justify-between"}>
                <div className={"flex flex-row items-center space-x-2"}>
                    <InfoIcon color={"primary"}/>
                    <Typography>Error type</Typography>
                </div>
                <Tooltip title={"Close dialog"}>
                    <IconButton onClick={() => setOpen(false)}>
                        <CloseIcon/>
                    </IconButton>
                </Tooltip>

            </DialogTitle>
            <DialogContent>
                {
                    <SyntaxHighlighter language={"JavaScript"} style={docco} className={"w-fit h-[50vh]"}>
                        {props.failes?.map((error: any) => JSON.stringify(error, undefined, 2))}
                    </SyntaxHighlighter>
                }
            </DialogContent>
        </Dialog>
    </>


}