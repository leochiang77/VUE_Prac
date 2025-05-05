import { createRouter, createWebHistory } from 'vue-router'
import AppLayout from '@/components/layout/AppLayout.vue'
import { useUserStore } from '@/stores/user'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/login',
      name: 'login',
      component: () => import("@/views/login/LoginIndex.vue"),
    },
    {
      path: '/',
      name: 'home',
      component: AppLayout,
      meta: { requiresAuth: true, title: "首頁" },
      children: [
        {
          path: "",
          name: "home_statistic",
          component: () => import("@/views/statistic/IndexView.vue"),
          meta: { title: "統計報表" }
        },
        {
          path: "statistic",
          name: "statistic",
          component: () => import("@/views/statistic/IndexView.vue"),
          meta: { title: "統計報表" }
        },
        {
          path: "explain",
          name: "explain",
          component: () => import("@/views/explain/IndexView.vue"),
          meta: { title: "認證評分說明" }
        },
        {
          path: "pplskill",
          name: "pplskill",
          component: () => import("@/views/pplskill/IndexView.vue"),
          meta: { title: "個人專業能力" }
        },
        {
          path: '/:pathMatch(.*)*',
          name: 'error',
          // route level code-splitting
          // this generates a separate chunk (About.[hash].js) for this route
          // which is lazy-loaded when the route is visited.
          component: () => import('../views/ErrorPage.vue'),
        },
      ]
    },
  ],
})

router.beforeEach((to, from, next) => {

  if (to.matched.some(r => r.meta?.requiresAuth)) {
    const store = useUserStore()
    if (!store.user) {
      next({ name: "login", query: { redirect: to.fullPath } })
      return
    }
  }
  next()
})

export default router