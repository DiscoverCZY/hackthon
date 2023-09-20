import { lazy } from 'react';

// project imports
import Layout from 'views/layout';
import Loadable from 'components/Loadable';

// dashboard routing
const Dashboard = Loadable(lazy(() => import('views/dashboard')));

// sample page routing
// const SamplePage = Loadable(lazy(() => import('views/sample-page')));

// ==============================|| MAIN ROUTING ||============================== //

const MainRoutes = {
  path: '/dashboard',
  element: <Layout />,
  children: [
    {
      path: 'default',
      element: <Dashboard/>
    },
    {
      path: 'test',
      element: <div>test</div>
    },
    /* {
      path: 'sample-page',
      element: <SamplePage />
    } */
  ]
};

export default MainRoutes;
