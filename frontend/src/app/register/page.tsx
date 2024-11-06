import { Button } from "@/components/ui/button";

export default function Home() {
    return (
      <>
        <div className="flex-1 bg-slate-100 flex items-center justify-center">
          <div className="w-[600px] rounded-lg h-[300px] flex p-5 bg-slate-200 flex-col justify-between">
            <h1 className="text-2xl font-bold">Register</h1>
            <div className="flex flex-col gap-5">
              <input placeholder="Email" className="p-2 rounded-md"></input>
              <input placeholder="Password" className="p-2 rounded-md"></input>
            </div>
            <Button className="align-bottom">
              Register 
            </Button>
          </div>
        </div>  
      </>
    
    );
}