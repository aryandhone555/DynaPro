import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

import Sidebar from "../../components/layout/Sidebar";
import Navbar from "../../components/layout/Navbar";

import { getResource } from "../../services/resourceService";

function ResourceDetails() {

    const { id } = useParams();

    const [resource, setResource] = useState(null);

    useEffect(() => {

        const loadResource = async () => {

            try {

                const data = await getResource(id);

                setResource(data);

            } catch (error) {

                console.error(error);

            }

        };

        loadResource();

    }, [id]);

    if (!resource) {

        return (
            <div className="flex items-center justify-center min-h-screen bg-slate-900 text-white">
                Loading...
            </div>
        );

    }

    return (

        <div className="flex min-h-screen bg-slate-900 text-white">

            <Sidebar />

            <div className="flex-1 flex flex-col">

                <Navbar />

                <main className="p-8">

                    <div className="flex justify-between items-start mb-10">

                        <div>

                            <p className="text-slate-400 mb-2">
                                ← Resources
                            </p>

                            <h1 className="text-4xl font-bold">
                                {resource.name}
                            </h1>

                            <div className="flex gap-3 mt-4">

                                <span className="bg-cyan-700 px-3 py-1 rounded-full">
                                    {resource.resource_type}
                                </span>

                                <span className="bg-slate-700 px-3 py-1 rounded-full">
                                    {resource.environment}
                                </span>

                            </div>

                        </div>

                        <div className="text-right">

                            <div
                                className={`px-5 py-2 rounded-full font-semibold ${
                                    resource.status === "GREEN"
                                        ? "bg-green-600"
                                        : resource.status === "AMBER"
                                        ? "bg-yellow-500 text-black"
                                        : "bg-red-600"
                                }`}
                            >
                                {resource.status}
                            </div>

                            <p className="text-slate-400 mt-3">
                                Last Updated
                            </p>

                            <p>
                                {new Date(resource.last_updated).toLocaleString()}
                            </p>

                        </div>

                    </div>

                </main>

            </div>

        </div>

    );

}

export default ResourceDetails;