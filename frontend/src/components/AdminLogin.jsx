import { useState } from "react"
import { useNavigate } from "react-router-dom"

const AdminLogin = () => {
    const navigate = useNavigate()
    const sub=(e)=>{
        
        console.log(username,pass)
        if(username=="admin" && pass=="admin123"){
            navigate("/admin")
        }
        else{
            alert("Incorrect credentials")
        }
    }
    const [username, setUsername] = useState("")
    const [pass, setPass] = useState("")
    
  return (
    <div className="mt-32">
        

<div className="max-w-sm mx-auto">
  <div className="mb-5">
    <label htmlFor="email" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Admin username</label>
    <input value={username} type="text" id="email" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"  required  onChange={(event)=>setUsername(event.target.value)}/>
  </div>
  <div className="mb-5">
    <label htmlFor="password" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Password</label>
    <input value={pass} type="password" id="password" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" required onChange={(event)=>setPass(event.target.value)} />
  </div>
  <div className="flex items-start mb-5">
    
  </div>
  <button  className="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800" onClick={sub}>Submit</button>
</div>

    </div>
  )
}

export default AdminLogin