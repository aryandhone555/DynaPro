function ResourceRow({ resource }) {

    return (

        <tr className="border-b hover:bg-slate-50">

            <td>{resource.name}</td>

            <td>{resource.resource_type}</td>

            <td>{resource.environment}</td>

            <td>{resource.status}</td>

            <td>{resource.metrics_count}</td>

            <td>{resource.last_updated}</td>

        </tr>

    );

}

export default ResourceRow;