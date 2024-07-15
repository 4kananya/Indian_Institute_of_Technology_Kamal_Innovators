import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";


function Trends({setProd, gender}) {
  const [products, setProducts] = useState([])
  // useEffect(()=>{
  //   axios.post("",{gender}).then(function (response) {
  //     setProducts(response);
  //   })
  // },[])
  const navigate = useNavigate();
  const a=[{"id":1,"productDisplayName":"HRX TSHIRT","Price":"300", "eco":"true", "img":"https://assets.myntassets.com/w_412,q_60,dpr_2,fl_progressive/assets/images/1987412/2022/11/21/cfd16572-9e2c-420e-8399-55568ad947f61669009324996-HRX-by-Hrithik-Roshan-Men-Black-Raglan-Sleeved-T-shirt-71166-1.jpg"},{"id":2,"productDisplayName":"PUMA trackpants","img":"https://assets.ajio.com/medias/sys_master/root/20221215/1Fzs/639b32d7f997ddfdbdd6a08f/-1117Wx1400H-469257388-grey-MODEL.jpg","Price":"400"}]
  const openProduct = (ele)=>{
    setProd(ele)
    navigate("/prod")
  }
  return (
    <div className="flex justify-center space-x-16 mt-20">
      {a.map((ele, index)=>(
        <div key={index} className={`h-96 w-60 shadow-lg hover:bg-slate-200 cursor-pointer `} onClick={()=>openProduct(ele)}>
            <img className="h-56 w-full" src={ele.img}></img>
            <div className="ml-4 mt-2">
              {ele.eco=="true"&&<div className="flex items-center"><img src="https://static.vecteezy.com/system/resources/thumbnails/010/852/913/small_2x/leaf-icon-vector-png.png" className="h-4 w-4 mr-2"></img> Eco-friendly </div>}
              <p className="font-bold">{ele.productDisplayName}</p>
              <p>₹ {ele.Price}</p>
              {ele.eco=="true"&&<button className="border-solid border-slate-500 border rounded-xl px-1 text-xs flex items-center mt-2">
                <img src="https://www.iconpacks.net/icons/1/free-coin-icon-794-thumb.png" className="h-4 w-4"></img>1.5X Myntra Coins</button>}
            </div>
        </div>
        

      ))}
    </div>
  )
}

export default Trends