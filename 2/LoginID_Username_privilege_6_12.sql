select distinct u.Login,u.Username ,nu.id,nu.name,privilege_id,pn.name from name2uid nu
join uid2perm up on nu.id = up.role_id
join perm2name pn on up.privilege_id =pn.id
join userrole u on u.role=nu.name
where u.Status != "已禁用"
order by u.Username,privilege_id asc;