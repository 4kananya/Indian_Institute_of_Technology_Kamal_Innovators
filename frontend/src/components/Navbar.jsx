import { useNavigate } from "react-router-dom";



function Navbar() {
  
  const navigate = useNavigate()

  return (
    <div className="shadow-sm min-h-20 w-full top-0 left-0 flex items-center ">
      <img
        src="https://cdn.iconscout.com/icon/free/png-256/free-myntra-2709168-2249158.png?f=webp&w=256"
        className="h-14 w-14 ml-12 cursor-pointer"
        onClick={()=>navigate("/")}
      ></img>
      <ul className="flex space-x-8 ml-16 text-xs font-bold text-slate-800">
        <li className="cursor-pointer">MEN</li>
        <li className="cursor-pointer">WOMEN</li>
        <li className="cursor-pointer">KIDS</li>
        <li className="cursor-pointer">HOME & LIVING</li>
        <li className="cursor-pointer">BEAUTY</li>
      </ul>
      <form className="max-w-md mx-auto">
        <label
          htmlFor="default-search"
          className="mb-1 text-sm font-medium text-gray-900 sr-only dark:text-white"
        >
          Search
        </label>
        <div className="relative">
          <div className="absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none">
            <svg
              className="w-4 h-4 text-gray-500 dark:text-gray-400"
              aria-hidden="true"
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 20 20"
            >
              <path
                stroke="currentColor"
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth="2"
                d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z"
              />
            </svg>
          </div>
          <input
            type="search"
            id="default-search"
            className="block w-96 p-2 ps-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
            placeholder="Search for products, brands and more"
            required
          />
        </div>
      </form>
      <img src="https://icons.veryicon.com/png/o/miscellaneous/qbi-product-icon-library/administrators-11.png" className="cursor-pointer h-6 w-6 mr-10 " onClick={()=>navigate("/admin-login")}></img>
    </div>
  );
};

export default Navbar;
