import { useEffect, useState } from "react";
import { getTrends } from "../../services/trendService";

import {
    ResponsiveContainer,
    LineChart,
    Line,
    XAxis,
    YAxis,
    CartesianGrid,
    Tooltip,
} from "recharts";

function TrendChart() {

    const [data, setData] = useState([]);

    useEffect(() => {

        const fetchData = async () => {

            try {

                const response = await getTrends();

                const formatted = response.map(point => ({

                    ...point,

                    time: new Date(point.timestamp)
                        .toLocaleTimeString([], {
                            hour: "2-digit",
                            minute: "2-digit"
                        })

                }));

                setData(formatted);

            } catch (err) {

                console.error(err);

            }

        };

        fetchData();

    }, []);

    return (

        <div className="bg-slate-800 rounded-xl p-6 h-[420px]">

            <h2 className="text-xl font-bold text-white mb-6">

                Resource Trends

            </h2>

            <ResponsiveContainer
                width="100%"
                height="90%"
            >

                <LineChart data={data}>

                    <CartesianGrid strokeDasharray="3 3" />

                    <XAxis dataKey="time" />

                    <YAxis />

                    <Tooltip />

                    <Line
                        type="monotone"
                        dataKey="value"
                        stroke="#3B82F6"
                        strokeWidth={3}
                        dot={false}
                    />

                </LineChart>

            </ResponsiveContainer>

        </div>

    );

}

export default TrendChart;