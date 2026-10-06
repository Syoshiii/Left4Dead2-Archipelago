const FL_KILLME = 67108864

if (!("m60toggle" in this))
    m60toggle <- {}

function m60toggle::OnGameEvent_round_start( params )
{
    for ( local gl; gl = Entities.FindByClassname( gl, "weapon_grenade_launcher_spawn" ); )
    {
        if ( NetProps.GetPropInt( gl, "m_fFlags" ) & FL_KILLME )
            continue

        if ( RandomInt( 1, 100 ) <= 50 )
        {
            SpawnEntityFromTable( "weapon_rifle_m60_spawn", {
                origin = gl.GetOrigin()
                angles = gl.GetAngles().ToKVString()
				count = 1
				solid = 6
            } )
            gl.Kill()
        }
    }
}

__CollectGameEventCallbacks( m60toggle )
