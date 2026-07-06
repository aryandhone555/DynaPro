import { useEffect, useState } from "react";

import Sidebar from "../../components/layout/Sidebar";
import Navbar from "../../components/layout/Navbar";
import ResourcesTable from "../../components/resources/ResourcesTable";

import { getResources } from "../../services/resourceService";

function Resources() {

    const [resources, setResources] = useState([]);
    const [search, setSearch] = useState("");
    const [statusFilter, setStatusFilter] = useState("ALL");
    const [typeFilter, setTypeFilter] = useState("ALL");
    const [environmentFilter, setEnvironmentFilter] = useState("ALL");
    const [loading, setLoading] = useState(false);

    const fetchResources = async () => {

        try {

            setLoading(true);

            const data = await getResources();

            setResources(data);

        } catch (error) {

            console.error(error);

        } finally {

            setLoading(false);

        }

    };

    useEffect(() => {

        fetchResources();

    }, []);

    const filteredResources = resources.filter((resource) => {

        const matchesSearch =
            resource.name
                .toLowerCase()
                .includes(search.toLowerCase());

        const matchesStatus =
            statusFilter === "ALL" ||
            resource.status === statusFilter;

        const matchesType =
            typeFilter === "ALL" ||
            resource.resource_type === typeFilter;

        const matchesEnvironment =
            environmentFilter === "ALL" ||
            resource.environment === environmentFilter;

        return (
            matchesSearch &&
            matchesStatus &&
            matchesType &&
            matchesEnvironment
        );

    });

    return (

        <div className="flex min-h-screen bg-slate-900 text-white">

            <Sidebar />

            <div className="flex-1 flex flex-col">

                <Navbar />

                <main className="flex-1 p-8">

                    <div className="mb-8">

                        <h1 className="text-4xl font-bold">
                            Resources
                        </h1>

                        <p className="text-slate-400 mt-2">
                            Monitor and manage all infrastructure resources.
                        </p>

                    </div>

                    <div className="mb-6 flex flex-wrap items-center gap-4">

                        <input
                            type="text"
                            placeholder="🔍 Search resources..."
                            value={search}
                            onChange={(e) => setSearch(e.target.value)}
                            className="
                                w-72
                                bg-slate-700
                                border
                                border-slate-600
                                rounded-lg
                                px-4
                                py-3
                                text-white
                                placeholder:text-slate-400
                                focus:outline-none
                                focus:ring-2
                                focus:ring-cyan-500
                            "
                        />

                        <select
                            value={statusFilter}
                            onChange={(e) => setStatusFilter(e.target.value)}
                            className="bg-slate-700 border border-slate-600 rounded-lg px-4 py-3"
                        >
                            <option value="ALL">All Status</option>
                            <option value="GREEN">Green</option>
                            <option value="AMBER">Amber</option>
                            <option value="RED">Red</option>
                        </select>

                        <select
                            value={typeFilter}
                            onChange={(e) => setTypeFilter(e.target.value)}
                            className="bg-slate-700 border border-slate-600 rounded-lg px-4 py-3"
                        >
                            <option value="ALL">All Types</option>
                            <option value="APP">APP</option>
                            <option value="DB">DB</option>
                        </select>

                        <select
                            value={environmentFilter}
                            onChange={(e) => setEnvironmentFilter(e.target.value)}
                            className="bg-slate-700 border border-slate-600 rounded-lg px-4 py-3"
                        >
                            <option value="ALL">All Environments</option>
                            <option value="PROD">PROD</option>
                            <option value="DEV">DEV</option>
                        </select>

                        <button
                            onClick={fetchResources}
                            disabled={loading}
                            className="
                                ml-auto
                                bg-cyan-600
                                hover:bg-cyan-500
                                disabled:bg-slate-600
                                disabled:cursor-not-allowed
                                px-5
                                py-3
                                rounded-lg
                                font-medium
                                transition
                            "
                        >
                            {loading ? "Refreshing..." : "🔄 Refresh"}
                        </button>

                    </div>

                    <div className="bg-slate-800 rounded-xl shadow-lg border border-slate-700 p-6">

                        <ResourcesTable
                            resources={filteredResources}
                        />

                    </div>

                </main>

            </div>

        </div>

    );

}

export default Resources;