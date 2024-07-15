import { useState } from "react";

const Admin = () => {
  const scrape = (ch) => {
    console.log(ch);
  };
  const [tab, setTab] = useState(1);
  const [blogOpen, setBlogOpen] = useState(false);
  return (
    <div>
      <ul className="flex flex-wrap text-sm font-medium text-center text-gray-500 border-b border-gray-200 dark:border-gray-700 dark:text-gray-400">
        <li className="me-2">
          <p
            className={`inline-block p-4 cursor-pointer ${
              tab == 1
                ? "text-blue-600 bg-gray-100 rounded-t-lg active"
                : "rounded-t-lg hover:text-gray-600 hover:bg-gray-50"
            }  `}
            onClick={() => setTab(1)}
          >
            Scrape
          </p>
        </li>
        <li className="me-2">
          <p
            className={`inline-block p-4 cursor-pointer ${
              tab == 2
                ? "text-blue-600 bg-gray-100 rounded-t-lg active"
                : "rounded-t-lg hover:text-gray-600 hover:bg-gray-50"
            }  `}
            onClick={() => setTab(2)}
          >
            Stock trend analyser
          </p>
        </li>
      </ul>
      {tab == 1 ? (
        <div className="flex mt-20 justify-center space-x-60">
          <div>
            <div>
              <button
              className="h-12 w-72 bg-rose-500 hover:bg-rose-400 text-white rounded-md mt-8"
              onClick={() => {
                scrape("B");
              }}
            >
              Scrape blogs
            </button>  
            </div>
            <div>
            {blogOpen && (
              <button className="h-12 w-72 bg-rose-500 hover:bg-rose-400 text-white rounded-md mt-8">
                Analyze
              </button>
            )}
            </div>
          </div>

          <button
            className="h-12 w-72 bg-rose-500 hover:bg-rose-400 text-white rounded-md mt-8"
            onClick={() => {
              scrape("I");
            }}
          >
            Scrape images
          </button>
        </div>
      ) : (
        <div className="flex mt-20 justify-center space-x-60">
          <button className="h-12 w-72 bg-rose-500 hover:bg-rose-400 text-white rounded-md mt-8">
            Analyze
          </button>
        </div>
      )}
    </div>
  );
};

export default Admin;
