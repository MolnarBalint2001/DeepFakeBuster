import {Record} from "../Record/Record.tsx";
import {FileUploader} from "react-drag-drop-files";
import {useCallback, useEffect, useState} from "react";
import {Button} from "@mui/material";
import SendIcon from '@mui/icons-material/Send';
import DeletIcon from "@mui/icons-material/Delete"
import {API_URL} from "../../globals/globals.ts";

import Aos from "aos"
import {Simulate} from "react-dom/test-utils";
import progress = Simulate.progress;


const testData: any[] = [
    {
        VideoName: "Video1.mp4",
        Result: false
    },
    {
        VideoName: "Video2.mp4",
        Result: true
    },
    {
        VideoName: "Video3.mp4",
        Result: false
    },
    {
        VideoName: "Video4.mp4",
        Result: true
    },
    {
        VideoName: "Video5.mp4",
        Result: true
    },
    {
        VideoName: "Video6.mp4",
        Result: false
    },
    {
        VideoName: "Video1.mp4",
        Result: false
    },
    {
        VideoName: "Video2.mp4",
        Result: true
    },
    {
        VideoName: "Video3.mp4",
        Result: false
    },
    {
        VideoName: "Video4.mp4",
        Result: true
    },
    {
        VideoName: "Video5.mp4",
        Result: true
    },
    {
        VideoName: "Video6.mp4",
        Result: false
    }
]

export const TestDatagrid = () => {


    useEffect(() => {
        Aos.init({
            once: true,
            duration: 1500
        })
    }, [])

    const [files, setFiles] = useState<File[]>([]);
    const [showDeleteBtn, setShowDeleteBtn] = useState<boolean>(true);


    const handleChange = (files: any) => {

        const uploadedFiles = []
        for (const [key, value] of Object.entries(files)) {
            (value as any).progress = false;
            (value as any).authenticated = null;
            console.log(value);
            uploadedFiles.push(value)
        }
        console.log(uploadedFiles)
        setFiles(uploadedFiles);
    }

    const handleDelete = (fileName: string) => {
        setFiles(prevState => files.filter((file: File) => file.name !== fileName));
    }


    const handleSubmit = useCallback(() => {
        setShowDeleteBtn(prevState => !prevState);
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
        <div
            className={"h-[80vh] w-[80%] shadow-2xl rounded-xl translate-y-[-5vh] bg-white flex flex-col items-center justify-start"}
            data-aos={"fade-right"}>

            <div className={"flex flex-col items-center  space-y-4 p-4 w-fit"}>
                <div>Choose files</div>
                <div className={"flex flex-row items-center justify-between space-x-2"}>
                    <FileUploader name={"file"} handleChange={handleChange} multiple={true} className={""}/>
                    <Button startIcon={<SendIcon/>} variant={"contained"} color={"primary"} onClick={handleSubmit}
                            className={""} size={"large"}>
                        Send
                    </Button>
                </div>
            </div>

            <div className={"w-full overflow-x-hidden h-[60vh] flex flex-col items-center space-y-2"}>
                {

                    files?.map((e: any, index: number) => {
                        return <Record key={index} progress={e.progress} showDeleteBtn={showDeleteBtn} videoName={e.name} result={e.authenticated}
                                       handleDelete={handleDelete}/>
                    })
                }
            </div>

        </div>
    );


}