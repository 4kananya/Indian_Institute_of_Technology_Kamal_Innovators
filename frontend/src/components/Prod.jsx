import { useEffect } from "react";

const Prod = ({ prod }) => {
    useEffect(()=>{
        //axios get request sending product id
      },[])
  return (
    <div className="ml-40 mb-40">
      <div className="flex  mt-20">
        <img className="h-96 w-72"></img>
        <div className="ml-80">
          <p className="font-bold text-2xl">{prod.Brand}</p>
          <p className="text-xl text-slate-600">{prod.productDisplayName}</p>
          <p className="font-bold text-2xl mt-6">{prod.Price}</p>
          <p className="font-bold text-green-600 text-sm mt-2">inclusive of all taxes</p>
          <button className="h-12 w-72 bg-rose-500 hover:bg-rose-400 text-white rounded-md mt-8">Add to Bag</button>
          <button className="h-12 w-52 border-solid border-slate-500 border rounded-md mt-8 ml-2 hover:border-2">Wishlist</button>

          <p className="font-bold text-2xl mt-32">Product Details</p>
      

<p>{prod[ "Ankle Height" ]}</p>
<p>{prod[ "Arch Type" ]}</p>
<p>{prod[ "articleType" ]}</p>
<p>{prod[ "Assorted" ]}</p>
<p>{prod[ "Back" ]}</p>
<p>{prod[ "Base Metal" ]}</p>
<p>{prod[ "Blouse" ]}</p>
<p>{prod[ "Border" ]}</p>
<p>{prod[ "Bottom Type" ]}</p>
<p>{prod[ "Cleats" ]}</p>
<p>{prod[ "Collar" ]}</p>
<p>{prod[ "Colour" ]}</p>
<p>{prod[ "Compartment Closure" ]}</p>
<p>{prod[ "Concern" ]}</p>
<p>{prod[ "Content" ]}</p>
<p>{prod[ "Coverage" ]}</p>
<p>{prod[ "Cushioning" ]}</p>
<p>{prod[ "Design" ]}</p>
<p>{prod[ "Details" ]}</p>
<p>{prod[ "Dial Material" ]}</p>
<p>{prod[ "Display" ]}</p>
<p>{prod[ "Distress" ]}</p>
<p>{prod[ "Fabric Purity" ]}</p>
<p>{prod[ "Fastening" ]}</p>
<p>{prod[ "Fastening and Back Detail" ]}</p>
<p>{prod[ "Features" ]}</p>
<p>{prod[ "Fine Jewellery" ]}</p>
<p>{prod[ "Finish" ]}</p>
<p>{prod[ "Fit" ]}</p>
<p>{prod[ "Formulation" ]}</p>
<p>{prod[ "Fragrance" ]}</p>
<p>{prod[ "gender" ]}</p>
<p>{prod[ "Heel Height" ]}</p>
<p>{prod[ "Heel Type" ]}</p>
<p>{prod[ "id" ]}</p>
<p>{prod[ "Insole" ]}</p>
<p>{prod[ "Length" ]}</p>
<p>{prod[ "Make" ]}</p>
<p>{prod[ "masterCategory" ]}</p>
<p>{prod[ "Material" ]}</p>
<p>{prod[ "Material Name" ]}</p>
<p>{prod[ "Minimum Shelf Life in Months" ]}</p>
<p>{prod[ "Minimum Threshold (%)" ]}</p>
<p>{prod[ "Minimum Usable Period in Months" ]}</p>
<p>{prod[ "Movement" ]}</p>
<p>{prod[ "Neck" ]}</p>
<p>{prod[ "Pattern" ]}</p>
<p>{prod[ "Reversible" ]}</p>
<p>{prod[ "Seam" ]}</p>
<p>{prod[ "season" ]}</p>
<p>{prod[ "Shape" ]}</p>
<p>{prod[ "Shoe Width" ]}</p>
<p>{prod[ "Size" ]}</p>
<p>{prod[ "Skin Tone" ]}</p>
<p>{prod[ "Skin Type" ]}</p>
<p>{prod[ "Sleeve" ]}</p>
<p>{prod[ "Sleeve Length" ]}</p>
<p>{prod[ "Sleeve Styling" ]}</p>
<p>{prod[ "sno" ]}</p>
<p>{prod[ "Sole Material" ]}</p>
<p>{prod[ "SPF" ]}</p>
<p>{prod[ "Sport" ]}</p>
<p>{prod[ "Stone Type" ]}</p>
<p>{prod[ "Strap Closure" ]}</p>
<p>{prod[ "Strap Material" ]}</p>
<p>{prod[ "Strap Style" ]}</p>
<p>{prod[ "Strap Type" ]}</p>
<p>{prod[ "Straps" ]}</p>
<p>{prod[ "Strength" ]}</p>
<p>{prod[ "subCategory" ]}</p>
<p>{prod[ "Surface Type" ]}</p>
<p>{prod[ "Toe Shape" ]}</p>
<p>{prod[ "Top Hemline" ]}</p>
<p>{prod[ "Top Type" ]}</p>
<p>{prod[ "Total Shelf Life in Months" ]}</p>
<p>{prod[ "Trends" ]}</p>
<p>{prod[ "Type" ]}</p>
<p>{prod[ "Units Per Bundle" ]}</p>
<p>{prod[ "usage" ]}</p>
<p>{prod[ "Volume in Litres" ]}</p>
<p>{prod[ "Waist Rise" ]}</p>
<p>{prod[ "Waistband" ]}</p>
<p>{prod[ "Water Resistance" ]}</p>
<p>{prod[ "Weave" ]}</p>
<p>{prod[ "Weave" ]}</p>
<p>{prod[ "year" ]}</p>




        </div>
      </div>
      <div>
        <p className="font-bold text-3xl mt-20 mb-6">Outfit recommender</p>
        <div className="h-56 w-52 shadow-lg hover:bg-slate-200 cursor-pointer" >
            <img className="h-56 w-full"></img>
            <div className="ml-4">
              
            </div>
        </div>
        
      </div>
    </div>
  );
};

export default Prod;
