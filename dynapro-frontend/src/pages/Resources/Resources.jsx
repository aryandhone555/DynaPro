import { useEffect, useState } from "react";

import Sidebar from "../../components/layout/Sidebar";
import Navbar from "../../components/layout/Navbar";
import ResourcesTable from "../../components/resources/ResourcesTable";

import { getResources } from "../../services/resourceService";

function Resources() {

    const [resources, setResources] = useState([]);

    useEffect(() => {

        const fetchResources = async () => {

            try {

                const data = await getResources();

                setResources(data);

            } catch (error) {

                console.error(error);

            }

        };

        fetchResources();

    }, []);

    return (

        <div className="flex min-h-screen bg-slate-100">

            <Sidebar />

            <div className="flex-1 flex flex-col">

                <Navbar />

                <main className="p-6">

                    <h1 className="text-3xl font-bold mb-6">
                        Resources
                    </h1>

                    <ResourcesTable resources={resources} />

                </main>

            </div>

        </div>

    );

}

export default Resources;