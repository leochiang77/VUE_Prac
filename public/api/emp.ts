import request from '@/utils/request'

let basedir = '/emp'
export const get_emp_data = (fab, empDict, action) => {
  let URL = ''
  if (action == 'fb_dept_gb_domainlevel') {
    URL = `${basedir}/fb_dept_gb_domainlevel/${fab}`
  } else if (action == 'fb_dept') {
    URL = `${basedir}/fb_dept/${fab}`
  } else if (action == 'ppl_info') {
    URL = `${basedir}/ppl_info/${fab}`
  }

  return request({
    method: 'GET',
    url: `${URL}`,
    params: empDict,
  })
}

export const put_emp_data = (fab, user_id, data, action) => {
  let URL = ''
  if (action == 'ppl_info') {
    URL = `${basedir}/ppl_info/${fab}/${user_id}`
  }

  return request({
    method: 'PUT',
    url: `${URL}`,
    data: data,
  })
}

export const put_domain_skill = (data, action) => {
  let URL = ''
  if (action == 'textarea') {
    URL = `${basedir}/daily_move_textarea`
  }
  return request({
    method: 'put',
    url: `${URL}`,
    data: data,
  })
}