import { useNavigate } from "react-router-dom";


const Home = ({setGender}) => {
    const navigate = useNavigate();
    const sendResp=(res)=>{
        setGender(res)
        navigate("/trends")
    }
  return (
    <div className="h-dvh flex pt-56 justify-center space-x-12 grad">
        <button className="rounded-full h-32 w-32 bg-blue-300 hover:bg-blue-400 flex justify-center items-center" onClick={(()=>sendResp("M"))}>
          <img src="https://www.iconpacks.net/icons/2/free-male-symbol-icon-2239-thumb.png" className="h-12 w-12"></img>
          </button>
        <button className="rounded-full h-32 w-32 bg-pink-300 hover:bg-pink-400 flex justify-center items-center" onClick={(()=>sendResp("F"))}>
        <img src="https://www.iconpacks.net/icons/2/free-female-symbol-icon-2240-thumb.png" className="h-14 w-14"></img>
        </button>
    </div>
  )
}

export default Home