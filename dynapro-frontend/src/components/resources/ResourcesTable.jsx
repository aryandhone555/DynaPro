import ResourceRow from "./ResourceRow";

function ResourcesTable({ resources }) {

    return (

        <div className="bg-white rounded-xl shadow">

            <table className="w-full">

                <thead>

                    <tr className="border-b">

                        <th>Name</th>
                        <th>Type</th>
                        <th>Environment</th>
                        <th>Status</th>
                        <th>Metrics</th>
                        <th>Last Updated</th>

                    </tr>

                </thead>

                <tbody>

                    {resources.map(resource => (

                        <ResourceRow
                            key={resource.id}
                            resource={resource}
                        />

                    ))}

                </tbody>

            </table>

        </div>

    );

}

export default ResourcesTable;