import { createRouter, createWebHistory, type RouteRecordRaw } from 'vue-router';
import DashboardLayout from '../layouts/DashboardLayout.vue';
import HomeView from '../views/HomeView.vue';

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    component: DashboardLayout, // The shell
    children: [
      {
        path: '',
        name: 'Dashboard',
        component: HomeView // Injects into DashboardLayout's <router-view>
      },
      // We will add the /runs and /settings views later
    ]
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;