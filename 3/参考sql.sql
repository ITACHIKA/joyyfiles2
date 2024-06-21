SELECT id, type, operator, operator_name, route, params, create_time,
      CASE 
        WHEN route = '//helloAddMoney/AddMoney' AND params LIKE '%request%' THEN JSON_EXTRACT(JSON_EXTRACT(params,'$.request'), '$.helloids')
       END AS helloids,
FROM json_split.action_journal1 
Limit 20000;