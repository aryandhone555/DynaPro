import {
  BrowserRouter,
  Routes,
  Route,
} from "react-router-dom";

import Login from "./pages/Login/Login";
import Dashboard from "./pages/Dashboard/Dashboard";
import ProtectedRoute from "./layouts/ProtectedRoute";
import Resources from "./pages/Resources/Resources";
import ResourceDetails from "./pages/Resources/ResourceDetails";

function App() {
  return (
    <BrowserRouter>

      <Routes>

        <Route
          path="/"
          element={<Login />}
        />

        <Route
          path="/dashboard"
          element={
            <ProtectedRoute>
              <Dashboard />
            </ProtectedRoute>
          }
        />

        <Route
          path="/resources"
          element={
            <ProtectedRoute>
              <Resources />
            </ProtectedRoute>
          }
        />

        <Route
          path="/resources/:id"
          element={<ResourceDetails />}
        />

      </Routes>

    </BrowserRouter>
  );
}

export default App;