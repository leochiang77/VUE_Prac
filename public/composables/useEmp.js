import { get_emp_data, put_emp_data } from '@/api/emp'
import { transFab } from '@/utils/utils'
import { useEmpStore } from '@/stores/emp'
const empStore = useEmpStore()
//import moment from 'moment'

const get_emp_data_fb_dept_gb_domainlevel = async (dept) => {
  const data = await get_emp_data(
    transFab(dept), { 'dept': dept },
    'fb_dept_gb_domainlevel',
  )
    .then((res) => {
      //console.log(res.data)
      return res.data

    })
    .catch((msg) => {
      console.log(msg)
      ElMessage.error('Get EMP [fb_dept_gb_domainlevel] Data Failed !!')
      throw new Error('Get EMP [fb_dept_gb_domainlevel] Data Failed !!')
    })

  empStore.saveEmpLevel(data)
}

const get_emp_data_fb_dept = async (dept) => {
  const data = await get_emp_data(
    transFab(dept), { 'dept': dept },
    'fb_dept',
  )
    .then((res) => {
      //console.log(res.data)
      return res.data

    })
    .catch((msg) => {
      console.log(msg)
      ElMessage.error('Get EMP [fb_dept] Data Failed !!')
      throw new Error('Get EMP [fb_dept] Data Failed !!')
    })

  empStore.saveEmp(data)
}

const get_emp_data_fb_userid = async (dept, user_id) => {
  let data = await get_emp_data(
    transFab(dept), { 'user_id': user_id },
    'ppl_info',
  )
    .then((res) => {
      //console.log(res.data)
      return res.data
    })
    .catch((msg) => {
      console.log(msg)
      ElMessage.error('Get EMP [ppl_info] Data Failed !!')
      throw new Error('Get EMP [ppl_info] Data Failed !!')
    })

  empStore.savePplinfo(data[0])
  return data[0]
}

const put_emp_data_fb_userid = async (dept, user_id, dictdata) => {
  let data = await put_emp_data(
    transFab(dept), user_id, dictdata, 'ppl_info',
  )
    .then((res) => {
      //console.log(res.data)
      return res.data
    })
    .catch((msg) => {
      console.log(msg)
      ElMessage.error('Put EMP [ppl_info] Data Failed !!')
      throw new Error('Put EMP [ppl_info] Data Failed !!')
    })

  return data
}

export { get_emp_data_fb_dept_gb_domainlevel, get_emp_data_fb_dept, get_emp_data_fb_userid, put_emp_data_fb_userid }