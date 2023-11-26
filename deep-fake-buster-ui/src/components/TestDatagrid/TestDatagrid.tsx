import {Record} from "../Record/Record.tsx";
import {FileUploader} from "react-drag-drop-files";
import {useCallback, useEffect, useState} from "react";
import {Button, Typography} from "@mui/material";
import SendIcon from '@mui/icons-material/Send';
import {API_URL} from "../../globals/globals.ts";
import {Paper} from "@mui/material";
import Aos from "aos"
import RestartAltIcon from '@mui/icons-material/RestartAlt';
import {CloudUpload} from "@mui/icons-material";

export const TestDatagrid = ({theme}) => {


    useEffect(() => {
        Aos.init({
            once: true,
            duration: 1500
        })
    }, [])

    const [files, setFiles] = useState<File[]>([]);
    const [showDeleteBtn, setShowDeleteBtn] = useState<boolean>(true);
    const [isSent, setIsSent] = useState<boolean>(false);
    const [uploadState, setUploadState] = useState<boolean>(true);

    const handleChange = async (files: any) => {

        const uploadedFiles = []
        for (const [key, value] of Object.entries(files)) {
            (value as any).progress = false;
            (value as any).authenticated = null;
            (value as any).videoSrc = await createBlob(value)
            console.log(value)
            uploadedFiles.push(value)
        }
        console.log(uploadedFiles)
        setFiles(uploadedFiles);
    }

    const handleDelete = (fileName: string) => {
        setFiles(prevState => files.filter((file: File) => file.name !== fileName));
    }


    const createBlob = async (file:any) =>{
        const arrayBuffer = await file.arrayBuffer()
        const blob =  new Blob([new Uint8Array(arrayBuffer)], {type: file.type });
        return URL.createObjectURL(blob)
    }

    const handleSubmit = useCallback(() => {
        setUploadState(false);
        setFiles(prevState => {
            const newArray = prevState.map((e: any) => {
                e.progress = true;
                return e;
            });
            return newArray;

        });
        files.forEach(async (file) => {
            const formData = new FormData();
            formData.append("file", file)
            try {
                await fetch(`${API_URL}/validate_video`, {
                    method: "POST",
                    headers: {},
                    body: formData
                })
                    .then((res)=>res.json())
                    .then((data)=>{
                        setFiles((prevState)=>{
                            const newArray:any = prevState.map((file)=>{
                                if (file.name === data.original_filename){
                                    (file as any).progress = false;
                                    (file as any).authenticated = data.authenticated;
                                    (file as any).failes = data.failes
                                }
                                return file
                            });
                            console.log(newArray)
                            return newArray;
                        })
                    });
                ;


            } catch (error) {
                console.log(error)
            }
        })


    }, [files]);


    return (
        <Paper  elevation={4}
               sx={{
                   backgroundColor:theme ? "#ffffff" : "#0f172a"
               }}
            className={`h-[80vh] w-[80%] !rounded-lg translate-y-[-5vh] bg-white flex flex-col items-center justify-start border-[1px] ${theme ? "border-slate-100" : "border-slate-800"} `}
            >

            <div className={"flex flex-col items-center  space-y-4 my-5 w-fit"}>
                <div className={"flex flex-row items-center justify-between space-x-2"}>
                    <FileUploader name={"file"} handleChange={handleChange} multiple={true} onSelect={()=>setShowDeleteBtn(true)}/>
                    <Button startIcon={<SendIcon/>} disabled={files.length === 0 ? true : false} variant={"contained"} color={"primary"} onClick={handleSubmit}
                            sx={{}} size={"large"}>
                        Send
                    </Button>
                    <Button startIcon={<RestartAltIcon/>}
                            onClick={()=>{
                                setFiles(prevState => []);
                                setUploadState(true);
                            }}
                            disabled={files.length === 0 ? true : false}
                            variant={"text"} color={"primary"}
                            className={""} size={"large"}>
                        {
                            uploadState ? "Clear uploads" : "Clear results"
                        }
                    </Button>
                </div>
            </div>

            <div className={"w-full overflow-x-hidden h-[60vh] flex flex-col items-center space-y-4"}>
                {

                    files.length === 0 ? <div className={"flex flex-col items-center mt-[20vh]"}>
                            <CloudUpload sx={{
                                height:100,
                                width:100,
                                color:theme ? "#d4d4d8" : "#334155"
                            }}/>
                            <Typography sx={{
                                color:theme ? "#d4d4d8" : "#334155"
                            }}>Upload videos and run tests</Typography>
                    </div> :
                    files?.map((e: any, index: number) => {
                        return <Record key={index}
                                       theme={theme}
                                       videoSrc={e.videoSrc}
                                       progress={e.progress}
                                       uploadState={uploadState}
                                       isSent={isSent}
                                       showDeleteBtn={showDeleteBtn}
                                       videoName={e.name}
                                       result={e.authenticated}
                                       failes={e.failes}
                                       handleDelete={handleDelete}
                        />
                    })
                }
            </div>

        </Paper>
    );


}